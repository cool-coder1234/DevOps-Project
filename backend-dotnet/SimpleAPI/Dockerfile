FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /src

# Disable external solution lookups completely
ENV DISABLE_CPM=true
ENV DOTNET_WORKSPACE_ROOT=/src
ENV DOTNET_CLI_TELEMETRY_OPTOUT=1

# Create standard empty solution wrapper inside container to trick the .NET engine
COPY SimpleAPI.csproj ./
RUN dotnet new sln && dotnet sln add SimpleAPI.csproj && dotnet restore SimpleAPI.csproj

# Copy all source files and publish cleanly
COPY . .
RUN dotnet publish SimpleAPI.csproj -c Release -o /app/publish --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

EXPOSE 5000
ENTRYPOINT ["dotnet", "SimpleAPI.dll", "--urls", "http://0.0.0.0:5000"]
