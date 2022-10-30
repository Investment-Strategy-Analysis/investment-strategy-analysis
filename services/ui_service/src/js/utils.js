/**
 * Round float percent with two symbols after dot
 * @param {number} percent
 * @returns {number?}
 */
export function formatFloat(percent) {
    if (percent === null) {
        return null;
    }
    return Math.round(percent * 1000) / 10;
}