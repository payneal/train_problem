class Train:
    
    def __init__(self):
        self.graph = {}
        
    # public
    def add_tracks(self, tracks):
        for track in tracks:
            self._add_to_graph( track)

    def show_graph(self):
        print("{}".format(self.graph))


    def get_distance(self, track):
        total = self._collect_path_distance(track) 
        if total: return total 
        return "NO SUCH ROUTE"


    def get_trips_max_limit(self, start, end, max_limit):
        count = 0
        for opt in self._get_trip_options(start, end):
            if len(opt) <= max_limit+1: count += 1
        return count

    
    def get_trips_equal(self, start, end, equal):
        count = 0
        for opt in self._get_trip_options(start, end):
            if  len(opt) == equal +1 : 
                count +=1
        return count 
    
    def get_shortest_route(self, start, end): 
        opts, short = self._get_trip_options(start, end), None
        for opt in opts:
            total = self.get_distance(opt)
            if short:  
                if total < short: short = total
            else: short = total
        return short


    def get_route_count(self, start, end, distance):
        opts =  self._get_trip_options(start, end) 
        start_end = self._build_trips_info(self.graph[start], start, end) 
        return self._calculate_route_count(opts, start_end, [], distance) 


    # private
    def _calculate_route_count(self, opts, start_end, answers, distance): 
        while True: 
            count, hold_opts = self._cycle_through_routes_created(
                    opts, start_end, answers, distance)
            if count ==0: break;
            opts = self._build_start_end_options(start_end, hold_opts)
        return len(answers)

      
    def _cycle_through_routes_created(self, opts, start_end, answers, distance): 
        hold_opts, count = {}, 0
        for opt in opts:
            count = self._check_route_vs_distance( 
                    opt, answers, hold_opts, count, distance)
        return count, hold_opts
    

    def _check_route_vs_distance( self, opt, answers, hold_opts, count, distance): 
        total = self.get_distance(opt)
        if total < distance and opt not in answers: 
            answers.append(opt)
            hold_opts[count] = opt
            count += 1
        return count


    def _get_trip_options(self, start, end):
        start_end, end_end = self._get_start_to_end_for_trips(start, end ) 
        return self._build_start_end_options(start_end, end_end)
    

    def _build_start_end_options(self, start_end, end_end):
        all_options = []
        for start in start_end:
             self._fill_options(all_options, start, start_end, end_end)
        return all_options


    def _fill_options(self, all_options, start, start_end, end_end):
        all_options.append(start_end[start])   
        for end in end_end:
            all_options.append(start_end[start][:-1] + end_end[end])
       

    def _get_start_to_end_for_trips( self, start, end ): 
        start_end = self._build_trips_info(self.graph[start], start, end) 
        end_end = self._build_trips_info( self.graph[end], end, end)
        return start_end, end_end


    def _build_trips_info( self, links, start, end): 
        answers = {}
        for link in range(len(links)):
            new_start = links[link]['destination'] 
            new_links = self.graph[new_start] 
            self._build_trip_answers(
                    answers, links, link, start, end, new_start, new_links)
        self._finalize_trip_answers(answers, end, new_start)
        return answers

    
    def _finalize_trip_answers(self, answers, end, new_start): 
        for answer in answers:
            if answers[answer][len(answers[answer])-1]  != end: 
                start_end = self._build_trips_info(
                        self.graph[new_start], new_start, end)
                if start_end: 
                    answers[answer] = answers[answer][:-1] + start_end[0]


    def _build_trip_answers(
            self, answers, links, link, start, end, new_start, new_links):
        if len(answers) > link: link =len(answers) 
        answers[link] = start + new_start
        self._trips_keep_searching(
                new_links, end, answers, link, start, new_start)
        

    def _trips_keep_searching(
            self, new_links, end, answers, link , start, new_start):
        for loop in range(len(new_links)):
            if end == new_links[loop]['destination']:
               self._add_next_path_to_trip(
                        answers, link, start, end, new_links, new_start, loop)
               
    
    def _add_next_path_to_trip( 
            self, answers, link, start, end, new_links, new_start, loop):
        answers[link + loop] = answers[link] + end       
        paths = self._build_trips_info( new_links, new_start, end)
        if len(paths) > 0:
            for path in paths: answers[link +loop + path ] = start + paths[path] 


    def _add_to_graph(self, track):
        if len(track) == 3: self._insert_to_graph(track[0], track[1], track[2])
    

    def _insert_to_graph(self, source, destination, length):
        if source not in self.graph: self.graph[source] = []
        self.graph[source].append({
            'destination': destination,'length':length})


    def _collect_path_distance(self, track): 
        total = 0
        for x in range (len(track) -1):
            add_value = self._collect_distance(track[x:x+2])
            if add_value: total += add_value
        if total >  0 and add_value: return total
        return False


    def _collect_distance(self, track):
        distance  = self._count_distance(track)
        if distance: return distance 
        elif distance is False: return False
        else: return  False


    def _get_total(self, track):
        values = self._get_possible_letters(self.graph[track[0]], track )
        if len(values) == 1:return values[0]["total"]
        elif len(values) > 1: return values
        return "NO SUCH ROUTE"


    def _get_possible_letters(self, source_link, track):
        values = self._get_connects(source_link, track)
        return self._add_totals(values, track);


    def _check_for_track(self, source, destination):
        for track in range(len(self.graph[source])):
            if destination == self.graph[source][track]['destination']:
                return  int(self.graph[source][track]['length'])
        return "NO SUCH ROUTE" 


    def _get_track_add_value(self, source, destination, count=0):
        if source in self.graph:
            add = self._check_for_track(source, destination)
            if isinstance(add, int):count += add
            else: return False
        if count == 0: return False
        return count


    def _count_distance(self, tracks):
        count = None
        for track in range( len(tracks) -1):
            source = tracks[track]
            destination = tracks[track +1]
            count  = self._get_track_add_value(source, destination)
        return count

 
    def _add_totals(self, values, track):
        for value in range(len(values)): 
            check = self._collect_distance(track[0]+values[x]['letter'])
            if check:
                values[values]['total'] = values[value]['distance'] + check
        return values 

        
    def _get_connects(self, source_link, track):
        values = []
        for value in range( len(source_link)):
            self._add_totals_to_connects(source_link[value], track, values) 
        return values            
    

    def _add_totals_to_connects(self, link, track, values):
        check = self._collect_distance(link["destination"] + track[1])
        if check: 
            letter = link["destination"]
            values.append({"letter": letter, 'distance':check} )
