def any_arrows(arrows):
    return len([1 for arrow in arrows if not 'damaged' in list(arrow.keys())])
