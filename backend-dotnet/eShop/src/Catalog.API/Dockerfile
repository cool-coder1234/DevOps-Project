FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src

COPY . .

RUN dotnet publish src/Catalog.API/Catalog.API.csproj -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

EXPOSE 5002
ENTRYPOINT ["dotnet", "Catalog.API.dll", "--urls", "http://0.0.0.0:5002"]
