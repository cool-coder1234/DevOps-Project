# Troubleshooting

## Docker Container Not Running

Check:

docker ps -a

Restart:

docker restart <container_name>

## Jenkins Build Failure

Check build logs from Jenkins dashboard.

## API Not Accessible

Verify backend container is running:

docker ps

Test API:

curl http://localhost/weatherforecast

## Frontend Not Loading

Verify frontend container:

docker ps

Check browser console for errors.
