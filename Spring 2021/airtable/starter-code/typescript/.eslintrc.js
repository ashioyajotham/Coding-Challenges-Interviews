module.exports = {
    parser: "@typescript-eslint/parser",
    parserOptions: {
        project: './tsconfig.json',
    },
    plugins: ['@typescript-eslint'],
    extends: [
        'eslint:recommended',
        'plugin:@typescript-eslint/eslint-recommended',
        'plugin:@typescript-eslint/recommended',
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
        '@typescript-eslint/array-type': 'off',
        '@typescript-eslint/prefer-interface': 'off',
        '@typescript-eslint/no-explicit-any': 'off',
        '@typescript-eslint/no-var-requires': 'off',
        '@typescript-eslint/no-use-before-define': ['warn', {
            functions: false,
        }],
        '@typescript-eslint/explicit-function-return-type': ['warn', {
            allowExpressions: true,
        }],
        '@typescript-eslint/no-empty-function': 'off',
        '@typescript-eslint/no-inferrable-types': 'off',
        '@typescript-eslint/member-delimiter-style': 'off',
    },
};
