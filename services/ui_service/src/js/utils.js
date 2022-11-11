export function formatFloat(percent) {
    if (percent === null) {
        return null;
    }
    return Math.round(percent * 1000) / 10;
}