import random
import copy

print("start")


class IndelingSystem:
    def __init__(self, list_of_users):
        self.list_of_users = list_of_users
        self.all_users = list(list_of_users.keys())
        self.reset()

    def reset(self):
        self.nog_in_te_delen = copy.copy(self.all_users)
        print(self.nog_in_te_delen)

    def deel_in(self):
        for key in self.all_users:

            possibilitys = self.succesor(key)
            going_to = random.sample(possibilitys, 1)[0]

            self.list_of_users[key]["going_to"] = going_to
            #             print("bezocht",self.list_of_users[key])
            self.list_of_users[going_to]["constraint"].append(key)
            self.nog_in_te_delen.remove(going_to)

    #             print(key ," will go to ", going_to,'\n',self.nog_in_te_delen)

    #         print(self.list_of_users)

    def succesor(self, key):
        succesors = copy.copy(self.nog_in_te_delen)
        if key in succesors:
            succesors.remove(key)
        for a in self.list_of_users[key]["constraint"]:
            if a in succesors:
                succesors.remove(a)

        #         print('possibilitys for',key,'are',succesors)
        return succesors

    def goal(self):
        bezocht = []
        print("\n\n checking")
        for key in self.list_of_users:
            to_ = self.list_of_users[key]["going_to"]
            if to_ in self.list_of_users[key]["constraint"]:
                return False
            else:
                pass
            if key == self.list_of_users[to_]["going_to"]:
                return False
            else:
                pass

        return True

    def find_by_whom(self):
        for key in self.all_users:
            for by in self.all_users:
                #                 print(by)
                if self.list_of_users[by]["going_to"] == key:
                    self.list_of_users[key]["by"] = by
                    break


def make_indeling(list_of_users):
    good = False
    i = 0
    while not good:
        try:
            indeling = IndelingSystem(list_of_users)
            indeling.deel_in()
            if indeling.goal():
                print("succes")
                good = True
        except Exception as e:
            if e is not "Sample larger than population or is negative":
                print(e)
            print("\n\n-------------\nNew round", i, "\n")
            i += 1
            del indeling

        if i > 100:
            print("not found")
            break

    indeling.find_by_whom()
    ouput_str = str(
        {
            key[-3:]: {
                "to": indeling.list_of_users[key]["going_to"][-3:],
                "by": indeling.list_of_users[key]["by"][-3:],
            }
            for key in indeling.list_of_users
        }
    )
    return indeling.list_of_users, ouput_str
