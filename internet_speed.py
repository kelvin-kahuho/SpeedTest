import typer
import speedtest
import time

app = typer.Typer()

def test_internet_speed():
    typer.echo("Starting speed test...\n")
    
    # Initialize the speed test object
    st = speedtest.Speedtest()
    
    # Find the best server
    typer.echo("Finding the best server based on ping...\n")
    st.get_best_server()
    
    typer.echo(f"Best server found: {st.results.server['host']} located in {st.results.server['country']}\n")
    
    # Perform a ping test
    typer.echo("Sending pings to test latency...\n")
    ping = st.results.ping
    time.sleep(1)  # Simulate delay for ping
    typer.echo(f"Ping: {ping:.2f} ms\n")
    
    # Perform a download test
    typer.echo("Measuring download speed...\n")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    typer.echo(f"Download speed: {download_speed:.2f} Mbps\n")
    
    # Perform an upload test
    typer.echo("Measuring upload speed...\n")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    typer.echo(f"Upload speed: {upload_speed:.2f} Mbps\n")
    
    return download_speed, upload_speed, ping


@app.command()
def speed():
    """
    Check the current internet speed with detailed steps.
    """
    typer.echo("Initializing internet speed test...\n")
    download, upload, ping = test_internet_speed()
    
    typer.echo("\nSpeed test completed successfully!")
    typer.echo(f"Results:")
    typer.echo(f"  - Download Speed: {download:.2f} Mbps")
    typer.echo(f"  - Upload Speed: {upload:.2f} Mbps")
    typer.echo(f"  - Ping: {ping:.2f} ms")

if __name__ == "__main__":
    app()
