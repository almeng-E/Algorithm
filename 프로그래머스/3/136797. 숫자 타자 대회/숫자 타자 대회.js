function solution(numbers) {
    const pos = {
        '1': [0, 0], '2': [0, 1], '3': [0, 2],
        '4': [1, 0], '5': [1, 1], '6': [1, 2],
        '7': [2, 0], '8': [2, 1], '9': [2, 2],
        '0': [3, 1]
    };

    function calcMove(from, to) {
        if (from === to) return 1;

        const [x1, y1] = pos[from];
        const [x2, y2] = pos[to];

        const dx = Math.abs(x1 - x2);
        const dy = Math.abs(y1 - y2);

        const diagonal = Math.min(dx, dy);
        const straight = Math.max(dx, dy) - diagonal;

        return diagonal * 3 + straight * 2;
    }

    let dp = new Map();
    dp.set('4,6', 0);

    for (const target of numbers) {
        const next = new Map();

        for (const [state, cost] of dp) {
            const [L, R] = state.split(',');

            if (target === L) {
                const key = `${L},${R}`;
                const nextCost = cost + 1;
                next.set(key, Math.min(next.get(key) ?? Infinity, nextCost));
                continue;
            }

            if (target === R) {
                const key = `${L},${R}`;
                const nextCost = cost + 1;
                next.set(key, Math.min(next.get(key) ?? Infinity, nextCost));
                continue;
            }

            {
                const key = `${target},${R}`;
                const nextCost = cost + calcMove(L, target);
                next.set(key, Math.min(next.get(key) ?? Infinity, nextCost));
            }

            {
                const key = `${L},${target}`;
                const nextCost = cost + calcMove(R, target);
                next.set(key, Math.min(next.get(key) ?? Infinity, nextCost));
            }
        }

        dp = next;
    }

    return Math.min(...dp.values());
}