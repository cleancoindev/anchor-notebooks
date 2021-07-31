from mantle import mantle


def native_token_balances(address: str):
    data = mantle(
        query="""
        query ($address: String!) {
          native_token_balances: BankBalancesAddress(Address: $address) {
            Result {
              Denom
              Amount
            }
          }
        }
    """,
        query_variables={
            'address': address
        }
    )

    result = {}

    for item in data['native_token_balances']['Result']:
        result[item['Denom']] = item['Amount']

    return result
