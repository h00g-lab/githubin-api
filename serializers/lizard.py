HEADER = 3

class Lizard():
  def __init__(self, data):
    self.files_count = 0
    self.functions = []
    self.averages = []
    self.totals = {}

    stopped_at = self.__set_functions(data)
    self.__set_averages(stopped_at, data)
    self.__set_totals(data)

  def __set_functions(self, data):
    lines_to_analyze = data[HEADER:]
    for index, line in enumerate(lines_to_analyze):
      if "file analyzed." in line:
        self.files_count = int(line.split(" ")[0])
        stopped_at = index + 1
        return stopped_at

      values = list(filter(None, line.split(" ")))
      function_data = values[5].split('@')
      function_name = function_data[0]
      function_lines = function_data[1]
      function_file = function_data[2];
      self.functions.append({
        'name': function_name,
        'lines': function_lines,
        'file': function_file,
        'nloc': values[0],
        'ccn': values[1],
        'token': values[2],
        'params_amount': values[3],
        'length': values[4]
      })

  def __set_averages(self, start_at, data):
    lines_to_analyze = data[2*HEADER+start_at:]
    for line in lines_to_analyze:
      values = list(filter(None, line.split(" ")))

      if(len(values) == 0):
        break

      self.averages.append({
        'nloc': values[0],
        'avg_nloc': values[1],
        'avg_ccn': values[2],
        'avg_token': values[3],
        'function_cnt': values[4],
        'file': values[5]
      })

  def __set_totals(self, data):
    last_line = data[-1]
    values = list(filter(None, last_line.split(" ")))
    self.totals = {
      'nloc': values[0],
      'avg_nloc': values[1],
      'avg_ccn': values[2],
      'avg_token': values[3],
      'function_cnt': values[4],
      'warning_cnt': values[5],
      'function_rt': values[6],
      'nloc_rt': values[7]
    }