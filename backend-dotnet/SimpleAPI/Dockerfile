FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /src

# Disable external tracking configurations strictly
ENV DISABLE_CPM=true
ENV DOTNET_WORKSPACE_ROOT=/src

# Copy project and restore using .NET 9 SDK
COPY SimpleAPI.csproj .
RUN dotnet restore SimpleAPI.csproj

# Copy all code and compile
COPY . .
RUN dotnet publish SimpleAPI.csproj -c Release -o /app/publish --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

EXPOSE 5000
ENTRYPOINT ["dotnet", "SimpleAPI.dll", "--urls", "http://0.0.0.0:5000"]
