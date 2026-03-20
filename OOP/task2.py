class Player:
    total_players = 0  

    def __init__(self, name):
        self.name = name
        self.clan = None         
        self.items = []          
        Player.total_players += 1

    def join_clan(self, clan):
        if self.clan:
            self.clan.members.remove(self)

        self.clan = clan
        clan.members.append(self)

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)
            item.owners.append(self)

    def become_leader(self, clan):
        clan.leader = self   

    def donate_to_clan(self, amount):
        if self.clan:
            self.clan.gold += amount

    @staticmethod
    def total():
        return Player.total_players


class Clan:
    total_clans = 0 

    def __init__(self, name):
        self.name = name
        self.members = []     
        self.leader = None    
        self.gold = 0
        Clan.total_clans += 1

    def add_member(self, player):
        player.join_clan(self)

    def set_leader(self, player):
        self.leader = player
        player.clan = self

    def reward_players(self, amount):
        for p in self.members:
            print(f"{p.name} received {amount} gold ")

    @staticmethod
    def total():
        return Clan.total_clans

class Item:
    total_items = 0 

    def __init__(self, name):
        self.name = name
        self.owners = []  
        Item.total_items += 1

    def give_to_player(self, player):
        if player not in self.owners:
            self.owners.append(player)
            player.items.append(self)

    def remove_from_player(self, player):
        if player in self.owners:
            self.owners.remove(player)
            player.items.remove(self)

    @staticmethod
    def total():
        return Item.total_items
