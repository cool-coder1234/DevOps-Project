# 1. SDK Image use karein ge build aur publish karne ke liye
FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src

# Pura eShop folder copy karein taake solution aur dependencies mil sakein
COPY backend-dotnet/eShop/ ./

# WebApp project ko publish karein (yeh 'out' folder khud banaye ga)
RUN dotnet publish src/WebApp/WebApp.csproj -c Release -o /app/publish

# 2. Runtime image par switch karein ge final size chota rakhne ke liye
FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app

# Build stage se publish shuda files copy karein
COPY --from=build /app/publish .

EXPOSE 5000
ENTRYPOINT ["dotnet", "WebApp.dll", "--urls", "http://0.0.0.0:5000"]
