import speedtest

def choose_server(st):
    print("Fetching nearby servers...\n")
    servers_dict = st.get_servers()

    # Flatten and sort all servers by distance
    all_servers = []
    for server_list in servers_dict.values():
        all_servers.extend(server_list)
    all_servers.sort(key=lambda s: s["d"])

    # Show top 5 closest servers
    top_servers = all_servers[:5]
    for i, server in enumerate(top_servers, start=1):
        print(f"{i}. {server['sponsor']} - {server['name']}, {server['country']} ({server['d']:.0f} km)")

    choice = input("\nSelect a server number (or press Enter for auto-best): ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(top_servers):
        selected = top_servers[int(choice) - 1]
        st.get_best_server(servers=[selected])
        print(f"\nUsing: {selected['sponsor']} - {selected['name']} ({selected['d']:.0f} km)\n")
    else:
        st.get_best_server()
        print(f"\nUsing auto-selected best server: {st.results.server['sponsor']} "
              f"({st.results.server['d']:.0f} km)\n")

def run_speed_test():
    st = speedtest.Speedtest()

    print("Retrieving speedtest.net configuration...")
    choose_server(st)

    print("Testing download speed...")
    download_speed = st.download() / 1_000_000

    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000

    ping = st.results.ping

    print(f"\nPing: {ping:.2f} ms")
    print(f"Download: {download_speed:.2f} Mbps")
    print(f"Upload: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    run_speed_test()
