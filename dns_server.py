import grpc
from concurrent import futures
import subprocess
import dns_service_pb2
import dns_service_pb2_grpc

class DnsResolverServicer(dns_service_pb2_grpc.DnsResolverServicer):
    def ResolveDomain(self, request, context):
        domain = request.domain
        
        result = subprocess.run(['dig', '+short', domain, '+trace'], stdout=subprocess.PIPE, text=True)
        
        
        ip_address = result.stdout.strip().split('\n')[0]

        if ip_address:
            return dns_service_pb2.DomainResponse(ip=ip_address, source="dns")
        else:
            return dns_service_pb2.DomainResponse(ip="0.0.0.0", source="dns")  # Sin respuesta válida

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dns_service_pb2_grpc.add_DnsResolverServicer_to_server(DnsResolverServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor gRPC corriendo en el puerto 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':  
    serve()
