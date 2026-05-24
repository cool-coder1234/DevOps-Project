FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Sahi context ke sath saari sub-folders aur props files image mein le kar aayen
COPY . .

# Ab bilkul stable framework package restore aur publish hoga
RUN dotnet publish src/WebApp/WebApp.csproj -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

EXPOSE 5000
ENTRYPOINT ["dotnet", "WebApp.dll", "--urls", "http://0.0.0.0:5000"]
