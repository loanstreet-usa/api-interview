from graphene import ObjectType, Schema, ID, Int, Float, Field, Interface, Mutation
from graphene import relay


class Loan(ObjectType):
    id = ID()
    amount = Float()
    interest_rate = Float()
    loan_length_months = Int()
    monthly_payment_amount = Float()

class Query(ObjectType):

    loans = Field(Loan)
    
    def resolve_loans(root, info):
        return Loan

def get_loans():
    return loan

schema = Schema(query=Query, mutation=Mutation)

# LoanSchema = GraphQLSchema(
#     query=queryType,
#     mutation=mutationType,
#     subscription=subscriptionType,
#     types=[humanType, droidType, reviewType, reviewInputType],
# )
# loan_schema = Schema(
#     query=LoanRootQuery,
#     mutation=LoanRootMutation,
#     subscription=LoanRootSubscription
# )



# class Loan(ObjectType):
#     """A LoanStreet loan"""

#     id = ID()
#     amount = Float()
#     interest_rate = Float()
#     loan_length_months = Int()
#     monthly_payment_amount = Float()

#     # @classmethod
#     # def get_loan():
#     #     # return loan.get(id)
#     #     pass

# def get_loan(id):
    

# class Query(ObjectType):
    
#     def resolve_loans(self):
#         extracted = extract()


# class Ship(graphene.ObjectType):
#     """A ship in the Star Wars saga"""

#     class Meta:
#         interfaces = (relay.Node,)

#     name = graphene.String(description="The name of the ship.")

#     @classmethod
#     def get_node(cls, info, id):
#         return get_ship(id)


# class ShipConnection(relay.Connection):
#     class Meta:
#         node = Ship


# class Faction(graphene.ObjectType):
#     """A faction in the Star Wars saga"""

#     class Meta:
#         interfaces = (relay.Node,)

#     name = graphene.String(description="The name of the faction.")
#     ships = relay.ConnectionField(
#         ShipConnection, description="The ships used by the faction."
#     )

#     def resolve_ships(self, info, **args):
#         # Transform the instance ship_ids into real instances
#         return [get_ship(ship_id) for ship_id in self.ships]

#     @classmethod
#     def get_node(cls, info, id):
#         return get_faction(id)


# class IntroduceShip(relay.ClientIDMutation):
#     class Input:
#         ship_name = graphene.String(required=True)
#         faction_id = graphene.String(required=True)

#     ship = graphene.Field(Ship)
#     faction = graphene.Field(Faction)

#     @classmethod
#     def mutate_and_get_payload(
#         cls, root, info, ship_name, faction_id, client_mutation_id=None
#     ):
#         ship = create_ship(ship_name, faction_id)
#         faction = get_faction(faction_id)
#         return IntroduceShip(ship=ship, faction=faction)


# class Query(graphene.ObjectType):
#     rebels = graphene.Field(Faction)
#     empire = graphene.Field(Faction)
#     node = relay.Node.Field()

#     def resolve_rebels(root, info):
#         return get_rebels()

#     def resolve_loans(root, info):
#         return Loan(id=1)


# class Mutation(graphene.ObjectType):
#     introduce_ship = IntroduceShip.Field()

