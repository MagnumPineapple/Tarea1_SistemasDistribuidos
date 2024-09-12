from flask import Flask, request, jsonify
import redis
import hashlib
import grpc
import dns_service_pb2
import dns_service_pb2_grpc

redis_connections = {
    0: redis.StrictRedis(host='localhost', port=6379, db=0),
    1: redis.StrictRedis(host='localhost', port=6381, db=0),
    2: redis.StrictRedis(host='localhost', port=6382, db=0),
    3: redis.StrictRedis(host='localhost', port=6383, db=0),
    4: redis.StrictRedis(host='localhost', port=6384, db=0),
    5: redis.StrictRedis(host='localhost', port=6385, db=0),
    6: redis.StrictRedis(host='localhost', port=6386, db=0),
    7: redis.StrictRedis(host='localhost', port=6387, db=0),
    8: redis.StrictRedis(host='localhost', port=6388, db=0),
}

app = Flask(__name__)

# Conexión al servidor gRPC
channel = grpc.insecure_channel('localhost:50051')
stub = dns_service_pb2_grpc.DnsResolverStub(channel)

def get_redis_connection(domain):
    partition_key = int(hashlib.md5(domain.encode()).hexdigest(), 16) % len(redis_connections)
    return redis_connections[partition_key]

@app.route('/resolve', methods=['GET'])
def resolve_domain():
    domain = request.args.get('domain') 
    if not domain:
        return jsonify({'error': 'Domain is required'}), 400

    
    redis_client = get_redis_connection(domain)
    cached_ip = redis_client.get(domain)

    if cached_ip:
        return jsonify({'domain': domain, 'ip': cached_ip.decode('utf-8'), 'source': 'cache'})

    
    grpc_request = dns_service_pb2.DomainRequest(domain=domain)
    response = stub.ResolveDomain(grpc_request)

    
    redis_client.set(domain, response.ip)   
    
    return jsonify({'domain': domain, 'ip': response.ip, 'source': response.source})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
