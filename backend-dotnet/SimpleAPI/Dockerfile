FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Force complete isolation and clear environment
ENV DISABLE_CPM=true
ENV DOTNET_WORKSPACE_ROOT=/src
ENV DOTNET_RUNNING_IN_CONTAINER=true

# Copy project file
COPY SimpleAPI.csproj .

# Force target official nuget source directly to bypass any proxy/local configs
RUN dotnet restore SimpleAPI.csproj --source https://api.nuget.org/v3/index.json

# Copy rest of the code and publish
COPY . .
RUN dotnet publish SimpleAPI.csproj -c Release -o /app/publish --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

EXPOSE 5000
ENTRYPOINT ["dotnet", "SimpleAPI.dll", "--urls", "http://0.0.0.0:5000"]
