import {resolve} from 'path';
import {defineConfig} from 'vite';
import solidPlugin from 'vite-plugin-solid';

const root = resolve(__dirname, 'src');
const outDir = resolve(__dirname, 'dist');

export default defineConfig({
    root: root,
    plugins: [solidPlugin()],
    resolve: {
        alias: {
            '~bootstrap': resolve(__dirname, 'node_modules/bootstrap'),
        }
    },
    server: {
        host: true,
        port: 5001,
        strictPort: true,
    },
    build: {
        target: "esnext",
        polyfillDynamicImport: false,
    },
});
