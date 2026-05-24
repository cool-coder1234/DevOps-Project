FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src

# Sahi dependency processing ke liye pura folder copy karein
COPY . .

# Puraane steps aur double quotes ka issue fix kar ke direct project compile karein
RUN dotnet publish src/WebApp/WebApp.csproj -c Release -o /app/publish

FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

EXPOSE 5000
ENTRYPOINT ["dotnet", "WebApp.dll", "--urls", "http://0.0.0.0:5000"]
