FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app

# Local system par bany hue 'out' folder se direct files copy karte hain
COPY eShop/src/WebApp/out/ .

EXPOSE 5000
ENTRYPOINT ["dotnet", "WebApp.dll", "--urls", "http://0.0.0.0:5000"]
