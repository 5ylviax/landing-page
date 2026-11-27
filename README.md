# Portfolio Website

My personal portfolio website, built with Flask and self-hosted on an Ubuntu server using Docker, Gunicorn, and Cloudflare Tunnel. A public Docker image is available through GitHub Container Registry (GHCR).

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS |
| Backend | Python, Flask |
| Hosting | Self-hosted Ubuntu Server |

## Run with Docker

The only requirement is [Docker](https://docs.docker.com/desktop/setup/install/windows-install/). On Windows or Linux, make sure Docker Desktop is running before executing the commands below.

On Linux, you may need to prefix the Docker commands in this README with `sudo`, unless your user is in the `docker` group.

The public image is available through [GitHub Packages](https://github.com/5ylviax?tab=packages) and can be pulled without a GitHub account or authentication.

### 1. Pull the image

```bash
docker pull ghcr.io/5ylviax/portfolio:latest
```

### 2. Create and start a container

```bash
docker run -d --name portfolio -p 127.0.0.1:4002:8000 ghcr.io/5ylviax/portfolio:latest
```

- `-d` runs the container in the background.
- `--name portfolio` assigns a name to the container. Choose a different name if `portfolio` is already in use.
- `-p 127.0.0.1:4002:8000` maps local port `4002` to port `8000` inside the container, where Gunicorn listens, and limits access to your own computer.

### 3. Open the site

Visit [http://localhost:4002](http://localhost:4002) in your browser.

### Update to the latest image

Pull the updated image, remove the old container, and create a new one:

```bash
docker pull ghcr.io/5ylviax/portfolio:latest
docker rm -f portfolio
docker run -d --name portfolio -p 127.0.0.1:4002:8000 ghcr.io/5ylviax/portfolio:latest
```

Pulling an updated image does not automatically update an existing container.

### Port notes

- **Different port:** If `4002` is already in use, change the host port. For example, `-p 127.0.0.1:4003:8000` makes the site available at http://localhost:4003. Keep the container port at `8000`.
- **Network access:** The default command limits access to your own computer. To allow access from other devices on your network, use `-p 4002:8000` instead.

## Build from source with Docker Compose

Use this option if you want to modify the source code and build your own image.

```bash
git clone https://github.com/5ylviax/portfolio.git
cd portfolio
docker compose up -d --build
```

Open [http://localhost:4002](http://localhost:4002).

After making changes, run the same command again to rebuild and recreate the container.

Stop and remove the Compose containers and networks:

```bash
docker compose down
```

If you already started a container named `portfolio` using `docker run`, remove it before starting the Compose project to avoid a name conflict.
