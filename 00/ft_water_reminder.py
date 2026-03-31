# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: seramaro <seramaro@student.42antananarivo  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/31 14:42:36 by seramaro          #+#    #+#              #
#    Updated: 2026/03/31 15:55:47 by seramaro         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder() -> None: 
    days_passed = int(input("Days since last watering: "))
    if days_passed > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
