# Jupyter notebooks explaining anchor queries / logics

These notes describe the graphql query and calculation logic of the anchor webapp as jupyter notebook.

> ⚠️ This project will be updated gradually whenever I have time. If there is anything you want to update first, please write it in Issue.

## Common

- [Token balances](./common_token_balances.ipynb)
- [Last Synced Height (block_height)](./common_last_synced_height.ipynb)

## Earn

- Main Screen
  - [Total Deposit](./earn_main_total_deposit.ipynb)
  - [Current APY](./earn_main_current_apy.ipynb)
  - [Expected Interest](./earn_main_expected_interest.ipynb)
- TODO: Deposit popup logics
- TODO: Withdraw popup logics

## Borrow

- Main Screen
  - [Collateral Value](./borrow_main_collateral_value.ipynb)
  - [Borrowed Value](./borrow_main_borrowed_value.ipynb)
  - TODO: Net APR
  - [LTV Chart](./borrow_main_ltv.ipynb)
  - [Collateral List](./borrow_main_collateral_list.ipynb)
- TODO: Provide collateral popup logics
- TODO: Withdraw collateral popup logics
- TODO: Borrow popup logics
- TODO: Repay popup logics

## Bond

- TODO: Mint logics
- TODO: Burn logics
- TODO: Claim logics

## Govern

- TODO: Main screen logics
- TODO: Trade ANC logics
- TODO: Gov stake logics
- TODO: ANC-UST LP logics

## My Page

- [Transaction History](./mypage_transaction_history.ipynb)

# Implementation in JavaScript

There is the `@terra-dev/mantle` with the same API as `mantle()` function in the Jupiter notebook. 

Note that if you would like to use the query in notebook the same in JS.

```js
import { mantle } from '@terra-dev/mantle'

const { marketState, govState } = await mantle({
  variables: {},
  mantleEndpoint: "https://tequila-mantle.anchorprotocol.com",
  wasmQuery: {
    marketState: {
      contractAddress: "terra15dwd5mj8v59wpj0wvt233mf5efdff808c5tkal", // moneyMarket.market
      query: {
        state: {}
      }
    },
    govState: {
      contractAddress: "terra16ckeuu7c6ggu52a8se005mg5c0kd2kmuun63cu", // gov
      query: {
        state: {}
      }
    }
  }
})
```

## Examples

- [JavaScript Basic Example](https://codesandbox.io/s/mantle-js-example-rs9xm)
- [TypeScript Basic Example](https://codesandbox.io/s/mantle-ts-example-hx59w)
- [With GraphQL Example](https://codesandbox.io/s/mantle-ts-graphql-example-eboln)
- [Use in Node.js (Koa Web Server Example)](https://codesandbox.io/s/mantle-nodejs-example-ed8c5)


# License

This software is licensed under the Apache 2.0 license. Read more about it [here](LICENSE).