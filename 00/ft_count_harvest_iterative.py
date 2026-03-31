# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: seramaro <seramaro@student.42antananarivo  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/31 14:43:56 by seramaro          #+#    #+#              #
#    Updated: 2026/03/31 14:55:18 by seramaro         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: ")) + 1
    for i in range(1, days):
        print("Day", i)
    print("Harvest time!")
