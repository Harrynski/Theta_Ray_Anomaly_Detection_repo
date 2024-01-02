txs = MT[['CreatedAt', 'TransactionId', 'Client', 'VendorCode', 
       'CollectMethod', 'TargetCountry', 'TargetCurrency', 'NetAmountUSD',
       'SendingAmount', 'RecipientAmount', 'SourceCountry',  'SenderDocument',
       'senderCountry', 'receiverDocument', 'receiverCountry', 'receiverBankAccountNumber']]

def client_mean_amount_p_user(df, client_name, amount_column = 'NetAmountUSD') -> float:
   return( round(df[df.Client==client_name][amount_column].mean(), 2))

def client_median_amount_p_user(df, client_name, amount_column = 'NetAmountUSD') -> float:
   return( round(df[df.Client==client_name][amount_column].median(), 2))

def vendor_median_amount_p_user(df, vendor_name, amount_column = 'NetAmountUSD') -> float:
   return( round(df[df.VendorCode==vendor_name][amount_column].median(), 2))

def vendor_mean_amount_p_user(df, vendor_name, amount_column = 'NetAmountUSD') -> float:
   return( round(df[df.VendorCode==vendor_name][amount_column].mean(), 2))

client_median_amounts = {}
for client in txs.Client.unique():
    median_amount = client_median_amount_p_user(txs, client)
    client_median_amounts[client] = median_amount

client_mean_amounts = {}
for client in txs.Client.unique():
    mean_amount = client_mean_amount_p_user(txs, client)
    client_mean_amounts[client] = mean_amount

vendor_median_amounts = {}
for vendor in txs.VendorCode.unique():
    median_amount = vendor_median_amount_p_user(txs, vendor)
    vendor_median_amounts[vendor] = median_amount

vendor_mean_amounts = {}
for vendor in txs.VendorCode.unique():
    mean_amount = vendor_mean_amount_p_user(txs, vendor)
    vendor_mean_amounts[vendor] = mean_amount

txs['meanClientAmount'] = txs.Client.apply(lambda x: client_mean_amounts[x])
txs['medianClientAmount'] = txs.Client.apply(lambda x: client_median_amounts[x])
txs['meanVendorAmount'] = txs.VendorCode.apply(lambda x: vendor_mean_amounts[x])
txs['medianVendorAmount'] = txs.VendorCode.apply(lambda x: vendor_median_amounts[x])
txs