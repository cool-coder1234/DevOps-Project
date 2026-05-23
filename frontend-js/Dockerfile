FROM node:20-alpine

WORKDIR /app

# Dependency files copy karte hain
COPY package*.json ./

# Agar yarn.lock mojood hai toh yarn use kar lete hain, nahi toh npm
COPY yarn.lock* ./

RUN if [ -f yarn.lock ]; then yarn install; else npm install; fi

# Baqi saara code copy karte hain
COPY . .

# Vite ka default dev port expose karte hain
EXPOSE 5173

# Vite app ko network par host karne ke liye --host flag zaroori hai
CMD ["if", "[", "-f", "yarn.lock", "];", "then", "yarn", "dev", "--host;", "else", "npm", "run", "dev", "--", "--host;", "fi"]
