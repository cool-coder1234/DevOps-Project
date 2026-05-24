FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src

# Central package versioning props file copy karte hain (NU1015 fix)
COPY ["eShop/Directory.Packages.props", "eShop/"]
COPY ["eShop/Directory.Build.props", "eShop/"]

# Saari zaroori dependency projects copy karte hain (Skipping project fix)
COPY ["eShop/src/Catalog.API/Catalog.API.csproj", "eShop/src/Catalog.API/"]
COPY ["eShop/src/eShop.ServiceDefaults/eShop.ServiceDefaults.csproj", "eShop/src/eShop.ServiceDefaults/"]
COPY ["eShop/src/EventBusRabbitMQ/EventBusRabbitMQ.csproj", "eShop/src/EventBusRabbitMQ/"]
COPY ["eShop/src/IntegrationEventLogEF/IntegrationEventLogEF.csproj", "eShop/src/IntegrationEventLogEF/"]

RUN dotnet restore "eShop/src/Catalog.API/Catalog.API.csproj"
COPY . .
WORKDIR "/src/eShop/src/Catalog.API"
RUN dotnet build "Catalog.API.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Catalog.API.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app
COPY --from=publish /app/publish .
EXPOSE 5002
ENTRYPOINT ["dotnet", "Catalog.API.dll", "--urls", "http://0.0.0.0:5002"]
