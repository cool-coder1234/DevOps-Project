FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src

# Pure backend-dotnet folder ko context ke mutabiq copy karein
COPY . .

# Ab accurate path par ja kar publish karein
RUN dotnet publish "backend-dotnet/eShop/src/WebApp/WebApp.csproj" -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

EXPOSE 5000
ENTRYPOINT ["dotnet", "WebApp.dll", "--urls", "http://0.0.0.0:5000"]
