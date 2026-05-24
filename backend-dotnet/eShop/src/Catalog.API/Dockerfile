FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src

# Pura repository structure copy karein
COPY . .

# Accurate path se direct publish karein (complex individual copies ki zaroorat nahi)
RUN dotnet publish "backend-dotnet/eShop/src/Catalog.API/Catalog.API.csproj" -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

EXPOSE 5002
ENTRYPOINT ["dotnet", "Catalog.API.dll", "--urls", "http://0.0.0.0:5002"]
