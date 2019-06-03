def dfs(tickets, graph, start, used_tickets):
    if start not in graph.keys():
        if len(tickets) == len(used_tickets):
            result = [used_tickets[0][0]]
            for way in used_tickets:
                result.append(way[1])
            return result
        else:
            False
    else:
        ways = [[start, dest] for dest in graph[start]]
        temp_ways = ways[:]
        for used_ticket in used_tickets:
            if used_ticket in temp_ways:
                temp_ways.remove(used_ticket)
        if not temp_ways:
            if len(tickets) == len(used_tickets):
                result = [used_tickets[0][0]]
                for way in used_tickets:
                    result.append(way[1])
                return result
            else:
                False
        else:
            for way in temp_ways:
                dest = way[1]
                temp_ticket = used_tickets[:]
                temp_ticket.append(way)
                if not dfs(tickets, graph, dest, temp_ticket):
                    continue
                else:
                    return dfs(tickets, graph, dest, temp_ticket)

def solution(tickets):
    graph = dict()
    for ticket in tickets:
        if ticket[0] in graph.keys():
            graph[ticket[0]].append(ticket[1])
        else:
            graph[ticket[0]] = [ticket[1]]
    for key in graph.keys():
        graph[key].sort()
    return dfs(tickets, graph, "ICN", [])

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets)) # [ICN, JFK, HND, IAD]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets)) # [ICN, ATL, ICN, SFO, ATL, SFD]
tickets = [["ICN", "JFK"], ["JFK", "IAD"], ["IAD", "ICN"], ["ICN", "JFK"]]
print(solution(tickets)) # ['ICN', 'JFK', 'IAD', 'ICN', 'JFK']
# tickets = [["ICN", "JFK"], ["JFK", "IAD"], ["IAD", "ICN"], ["ICN", "IAE"]]
# print(solution(tickets)) # ['ICN', 'JFK', 'IAD', 'ICN', 'JFK']
# tickets = [["ICN", "JFK"], ["JFK", "IAD"], ["IAD", "ICN"], ["ICN", "JFK"]]
# print(solution(tickets)) # ['ICN', 'JFK', 'IAD', 'ICN', 'JFK']
