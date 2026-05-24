FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /src

# Disable tracking configurations and central props completely
ENV DISABLE_CPM=true
ENV IMPORT_DIRECTORY_BUILD_PROPS=false
ENV IMPORT_DIRECTORY_PACKAGES_PROPS=false

COPY SimpleAPI.csproj .
RUN dotnet restore SimpleAPI.csproj

COPY . .
RUN dotnet publish SimpleAPI.csproj -c Release -o /app/publish --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

EXPOSE 5000
ENTRYPOINT ["dotnet", "SimpleAPI.dll", "--urls", "http://0.0.0.0:5000"]
