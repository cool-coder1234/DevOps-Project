# .NET 8.0 SDK use karein taake packages compatible rahein
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Sahi relative path se saari files image mein copy karein
COPY . .

# Direct project compile aur publish karein
RUN dotnet publish src/Catalog.API/Catalog.API.csproj -c Release -o /app/publish

# Final light-weight production runtime target
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

EXPOSE 5002
ENTRYPOINT ["dotnet", "Catalog.API.dll", "--urls", "http://0.0.0.0:5002"]
