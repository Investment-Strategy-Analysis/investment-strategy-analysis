/**
 * Round float percent with two symbols after dot
 * @param {number} percent
 * @returns {number?}
 */
export function formatFloat(percent) {
    if (percent === null) {
        return null;
    }
    return Math.round(percent * 10) / 1000;
}

/**
 * Round float value with two symbols after dot
 * @param {number} percent
 * @returns {number?}
 */
export function formatFloatValue(percent) {
    if (percent === null) {
        return null;
    }
    return Math.round(percent * 100) / 100;
}
