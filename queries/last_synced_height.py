from mantle import mantle


def last_synced_height():
    result = mantle(
        query="""
        query {
          last_synced_height: LastSyncedHeight
        }
      """
    )

    return result['last_synced_height']
