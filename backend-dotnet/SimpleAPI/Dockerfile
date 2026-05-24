FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /src

# Force .NET to completely ignore ANY Directory.Build.props or Directory.Packages.props
ENV IMPORT_DIRECTORY_BUILD_PROPS=false
ENV IMPORT_DIRECTORY_PACKAGES_PROPS=false
ENV DISABLE_CPM=true
ENV DOTNET_WORKSPACE_ROOT=/src

# Copy project file cleanly
COPY SimpleAPI.csproj .
RUN dotnet restore SimpleAPI.csproj

# Copy everything else and publish
COPY . .
RUN dotnet publish SimpleAPI.csproj -c Release -o /app/publish --no-restore

FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

EXPOSE 5000
ENTRYPOINT ["dotnet", "SimpleAPI.dll", "--urls", "http://0.0.0.0:5000"]
