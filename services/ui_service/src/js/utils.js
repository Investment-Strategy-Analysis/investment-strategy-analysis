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

export function timeToInt(id) {
    return {
        "YEAR_1": 365,
        "YEAR_3": 365 * 3,
        "YEAR_5": 365 * 5,
        "YEAR_10": 365 * 10,
    }[id];
}
