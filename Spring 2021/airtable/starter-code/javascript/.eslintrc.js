module.exports = {
    env: {
        node: true,
    },
    parserOptions: {
        ecmaVersion: 2015,
    },
    extends: [
        'eslint:recommended',
    ],
    rules: {
        'eqeqeq': 'warn',
        'semi': 'warn',
        'semi-spacing': 'warn',
        'indent': ['warn', 4, {
            SwitchCase: 1,
        }],
        'comma-dangle': ['warn', 'always-multiline'],
        'no-constant-condition': ['warn', {
            checkLoops: false,
        }],
    },
};
