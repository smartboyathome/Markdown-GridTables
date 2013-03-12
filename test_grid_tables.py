import markdown

markdown_table = \
"""
+-------+----------+------+
| Table Headings   | Here |
+-------+----------+------+
| Sub   | Headings | Too  |
+=======+==========+======+
| cell  | column spanning |
+ spans +----------+------+
| rows  | normal   | cell |
+-------+----------+------+
| multi | cells can be    |
| line  | *formatted*     |
|       | **paragraphs**  |
| cells |                 |
| too   |                 |
+-------+-----------------+"""[1:]
html_table = \
"""<table>
<thead>
<tr>
<th colspan="2" rowspan="1">
<p>Table Headings</p>
</th>
<th colspan="1" rowspan="1">
<p>Here</p>
</th>
</tr>
<tr>
<th colspan="1" rowspan="1">
<p>Sub</p>
</th>
<th colspan="1" rowspan="1">
<p>Headings</p>
</th>
<th colspan="1" rowspan="1">
<p>Too</p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="1" rowspan="2">
<p>cell
spans
rows</p>
</td>
<td colspan="2" rowspan="1">
<p>column spanning</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>normal</p>
</td>
<td colspan="1" rowspan="1">
<p>cell</p>
</td>
</tr>
<tr>
<td colspan="1" rowspan="1">
<p>multi
line</p>
<p>cells
too</p>
</td>
<td colspan="2" rowspan="1">
<p>cells can be
<em>formatted</em>
<strong>paragraphs</strong></p>
</td>
</tr>
</tbody>
</table>"""

md = markdown.Markdown(extensions=['grid_tables'])
result = md.convert(markdown_table)
#print result
#with open('test_grid_tables.html', 'w') as f:
#    f.write(result + '<style>table, tr, td, th {border: 1px solid black;}</style>')
assert result == html_table
