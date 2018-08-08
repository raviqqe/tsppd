module.exports = {
  collectCoverage: true,
  moduleFileExtensions: ["ts", "js"],
  transform: {
    "^.+\\.ts$": "ts-jest"
  },
  testEnvironment: "node",
  testMatch: ["<rootDir>/src/**/__tests__/*.ts"]
};
