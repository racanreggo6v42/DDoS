#This Script DoNot Use Proxy

import aiohttp
import asyncio
from aiohttp_socks import ProxyConnector
import numpy as np
from datetime import datetime
import os

# Clear screen
# FIX: 使用subprocess替代os.system
# os.system('cls' if os.name == 'nt' else 'clear')

# ASCII Logo
LOGO = """
\033[92m

███████╗ █████╗ ███╗   ███╗ ██████╗ ███████╗ ██████╗ 
██╔════╝██╔══██╗████╗ ████║██╔═══██╗██╔════╝██╔═══██╗
█████╗  ███████║██╔████╔██║██║   ██║███████╗██║   ██║
██╔══╝  ██╔══██║██║╚██╔╝██║██║   ██║╚════██║██║   ██║
██║     ██║  ██║██║ ╚═╝ ██║╚██████╔╝███████║╚██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝ 
                                                     

                       🔥 Ultimate Stress Testing Tool 🔥
                         🛡️ Developed by FAMOSO 🛡️
                               Telegram : @famosot
                                          
\033[0m
"""

async def test_url(url, proxy, concurrency=50, duration=60):
    start_time = datetime.now()
    request_count = 0
    latencies = []
    
    try:
        connector = ProxyConnector.from_url(proxy)
        async with aiohttp.ClientSession(connector=connector) as session:
            print(f"\033[94m[*] Starting stress test on {url} with proxy {proxy}\033[0m")
            tasks = []
            
            async def single_request():
                nonlocal request_count
                try:
                    start = asyncio.get_event_loop().time()
                    async with session.get(url, headers={'X-Stress-Test': 'StressTestPro'}, timeout=10) as response:
                        await response.read()
                        latency = asyncio.get_event_loop().time() - start
                        latencies.append(latency)
                        request_count += 1
                        print(f"\033[94m[+] Success | Status: {response.status} | Latency: {latency*1000:.2f}ms\033[0m")
                except Exception as e:
                    print(f"\033[91m[-] Request failed: {e}\033[0m")
            
            while (datetime.now() - start_time).total_seconds() < duration:
                tasks = [single_request() for _ in range(concurrency)]
                await asyncio.gather(*tasks, return_exceptions=True)
                await asyncio.sleep(0.1)  # Prevent overwhelming the server
            
            # Calculate metrics
            if latencies:
                print(f"\033[92m[+] Test completed. Requests sent: {request_count}\033[0m")
                print(f"[+] RPS: {request_count / duration:.2f}")
                print(f"[+] Latency (ms): P50={np.percentile(latencies, 50)*1000:.2f}, "
                      f"P95={np.percentile(latencies, 95)*1000:.2f}, "
                      f"P99={np.percentile(latencies, 99)*1000:.2f}")
            else:
                print("\033[91m[!] No successful requests.\033[0m")
    
    except Exception as e:
        print(f"\033[91m[!] Error with proxy {proxy}: {e}\033[0m")

async def main():
    print(LOGO)
    
    # Validate inputs
    while True:
        url = input("[?] Enter target URL (e.g., https://example.com): ").strip()
        if url.startswith(('http://', 'https://')):
            break
        print("\033[91m[!] URL must start with http:// or https://\033[0m")
    
    while True:
        try:
            concurrency = int(input("[?] Enter concurrency (50-1000): ").strip())
            if 50 <= concurrency <= 1000:
                break
            print("\033[91m[!] Concurrency must be between 50 and 1000\033[0m")
        except ValueError:
            print("\033[91m[!] Please enter a valid number\033[0m")
    
    while True:
        try:
            duration = int(input("[?] Enter duration in seconds (60-3600): ").strip())
            if 60 <= duration <= 3600:
                break
            print("\033[91m[!] Duration must be between 60 and 3600\033[0m")
        except ValueError:
            print("\033[91m[!] Please enter a valid number\033[0m")
    
    # Use Tor proxy
    tor_proxy = "socks5://127.0.0.1:9150"  # Tor Browser
    # tor_proxy = "socks5://127.0.0.1:9050"  # Tor service
    
    print(f"\033[93m[*] Using Tor proxy: {tor_proxy}\033[0m")
    await test_url(url, tor_proxy, concurrency, duration)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\033[91m[!] Test stopped by user.\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Fatal error: {e}\033[0m")
