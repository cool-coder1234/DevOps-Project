FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src

# Sahi paths ke sath props files copy karein
COPY ["backend-dotnet/eShop/Directory.Packages.props", "backend-dotnet/eShop/"]
COPY ["backend-dotnet/eShop/Directory.Build.props", "backend-dotnet/eShop/"]

# Saari dependency projects ke paths correct kar diye hain
COPY ["backend-dotnet/eShop/src/Catalog.API/Catalog.API.csproj", "backend-dotnet/eShop/src/Catalog.API/"]
COPY ["backend-dotnet/eShop/src/eShop.ServiceDefaults/eShop.ServiceDefaults.csproj", "backend-dotnet/eShop/src/eShop.ServiceDefaults/"]
COPY ["backend-dotnet/eShop/src/EventBusRabbitMQ/EventBusRabbitMQ.csproj", "backend-dotnet/eShop/src/EventBusRabbitMQ/"]
COPY ["backend-dotnet/eShop/src/IntegrationEventLogEF/IntegrationEventLogEF.csproj", "backend-dotnet/eShop/src/IntegrationEventLogEF/"]

RUN dotnet restore "backend-dotnet/eShop/src/Catalog.API/Catalog.API.csproj"
COPY . .
WORKDIR "/src/backend-dotnet/eShop/src/Catalog.API"
RUN dotnet build "Catalog.API.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Catalog.API.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app
COPY --from=publish /app/publish .
EXPOSE 5002
ENTRYPOINT ["dotnet", "Catalog.API.dll", "--urls", "http://0.0.0.0:5002"]
