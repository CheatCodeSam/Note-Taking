import { defineConfig } from "vite";

export default defineConfig({
  base: "/static/",
  server: {
    host: "127.0.0.1",
    port: 3000,
    open: false,
    watch: {
      usePolling: false,
      disableGlobbing: false,
    },
  },
  publicDir: "publicDir",
  build: {
    manifest: true,
    outDir: "./build",
    rollupOptions: {
      input: {
        mykey: "./src/main.js",
        favicon: "./publicDir/favicon.ico",
      },
    },
  },
});
