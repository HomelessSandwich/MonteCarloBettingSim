def print_stats(num_broke, num_profitors, sample_size, profits, loses, type):
    broke_percent = (num_broke / sample_size) * 100
    profit_percent = (num_profitors / sample_size) * 100
    try:
        survive_profit_percent = (num_profitors / (sample_size - num_broke)) * 100
    except ZeroDivisionError:
        survive_profit_percent = 0
    try:
        avg_profit = sum(profits) / len(profits)
    except ZeroDivisionError:
        avg_profit = 0
    try:
        avg_loses = sum(loses) / len(loses)
    except ZeroDivisionError:
        avg_loses = 0

    print(f'\n{type} Percentage Broke: {broke_percent}%')
    print(f'{type} Percentage Profited: {profit_percent}%')
    print(f'{type} Percentage Survivors Profited: {survive_profit_percent}%')
    print(f'{type} Avergage Profit: {avg_profit}')
    print(f'{type} Avergage Loses: {avg_loses}')
    print(f'    {type} Expected Profit: {avg_profit * (profit_percent/ 100)}')
    print(f'    {type} Expected Loss: {avg_loses * (1 - (profit_percent / 100))}')
