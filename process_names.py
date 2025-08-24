import csv
import glob
import os
# Read name list

header = """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Guest List - Oshani & Lisitha Wedding</title>

    <!-- Custom fonts for this template -->
    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link
        href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
        rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/sb-admin-2.min.css" rel="stylesheet">

    <!-- Custom styles for this page -->
    <link href="vendor/datatables/dataTables.bootstrap4.min.css" rel="stylesheet">

</head>

<body id="page-top">

    <!-- Page Wrapper -->
    <div id="wrapper">


        <!-- End of Sidebar -->

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">
                

                <!-- Begin Page Content -->
                <div class="container-fluid">

                    <!-- Page Heading -->
                    <h1 class="h3 mb-2 text-gray-800">Oshani & Lisitha Wedding</h1>
                    <div >
                      <details id="table_detail">
                        <summary>Table Plan</summary>
                        <object data="lisitha_wedding.svg" type="image/svg+xml"
                    id="tables" width="100%" height="100%" style="border: none"></object>
                      </details>
                    </div>						
                    <p class="mb-4">Search for guests and their table numbers.</p>
					<div class="col-sm-6 mb-3 mb-sm-0">
						<input type="text" class="form-control form-control-user" id="myInput" onkeyup="filterName()"
							placeholder="Search for names...">
					</div>	
					<br>					
                    <!-- DataTales Example -->
                    <div class="card shadow mb-4">
                        <div class="card-header py-3">
                            <h6 class="m-0 font-weight-bold text-primary">Guest List</h6>
                        </div>
                        <div class="card-body">
                            <div class="table-responsive">
                                <table class="table table-bordered" id="myTable" width="100%" cellspacing="0">
                                    <thead>
                                        <tr>
                                            <th>Name</th>
                                            <th>Table Number</th>
                                        </tr>
                                    </thead>
                                    <tbody>
"""


footer = """
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>

                </div>
                <!-- /.container-fluid -->

            </div>
            <!-- End of Main Content -->

            <!-- Footer -->
            <footer class="sticky-footer bg-white">
                <div class="container my-auto">
                    <div class="copyright text-center my-auto">
                        <span>Copyright &copy; Uvindu Wijesinghe 2025</span>
                    </div>
                </div>
            </footer>
            <!-- End of Footer -->

        </div>
        <!-- End of Content Wrapper -->

    </div>
    <!-- End of Page Wrapper -->

    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
        <i class="fas fa-angle-up"></i>
    </a>

    <!-- Logout Modal-->
    <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
                    <button class="close" type="button" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">×</span>
                    </button>
                </div>
                <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
                <div class="modal-footer">
                    <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
                    <a class="btn btn-primary" href="login.html">Logout</a>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap core JavaScript-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="js/sb-admin-2.min.js"></script>

    <!-- Page level plugins -->
    <script src="vendor/datatables/jquery.dataTables.min.js"></script>
    <script src="vendor/datatables/dataTables.bootstrap4.min.js"></script>

    <!-- Page level custom scripts -->
    <script src="js/demo/datatables-demo.js"></script>


<script>

var svgDoc
function getTableById(elementId) {

    if (!svgDoc) return null;
	
    parentEl = svgDoc.getElementById(elementId)
	return parentEl.firstChild.firstChild;
}

async function setTableGreen(tableID){
  // Open the details element
  document.getElementById("table_detail").setAttribute("open", "true");
  // Scroll to top of page
  window.scrollTo({ top: 0, behavior: 'smooth' });
  // Wait 200ms for the SVG to load so that svgDoc is ready
  await new Promise(r => setTimeout(r, 200));

  // Reset all table elements to have the normal properties
	for (let i = 1; i < 34; i++) {
		table_el = getTableById("cell-table"+i)
		table_el.setAttribute("fill","transparent")
		table_el.setAttribute("style","stroke: rgb(215,155,0)")
		table_el.setAttribute("stroke-width","7")
	}
	
	// Highlight the current table with different fill, border, and border size
	table_el = getTableById("cell-table"+tableID)
	table_el.setAttribute("fill","navy")
	table_el.setAttribute("style","stroke: #0AF5A3")
	table_el.setAttribute("stroke-width","15")
}

// Get the object ID for the SVG
const obj = document.getElementById("tables");

// Setup svgDoc variable when object loads to make SVG accessible
obj.addEventListener("load", () => {
    svgDoc = obj.contentDocument;
    if (!svgDoc) {
        console.error("SVG not accessible — check same-origin or file path");
        return;
    }
});

// A function to filter the name-table_number table based on the name provided
function filterName() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}
</script>


</body>

</html>
"""
row_data = """
										  <tr>
											<td>{name}</td>
											<td onclick="setTableGreen({table})" href="#"><a href="#">{table}</a></td>
										  </tr>
  """
all_rows = ""
with open('Invite List.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	counter = 0
	nameList={}
	for row in spamreader:
		if counter == 0:
			counter = counter + 1
			continue
		# Remove titles from names so that alphabetic ordering can be done
		data=row[0]
		data=data.replace("Mr. & Mrs. ", "")
		#print("1 " + data)
		data=data.replace("Mrs. ", "")
		#print("2 " + data)		
		data=data.replace("Mr. ", "")
		#print("3 " + data)	
		data=data.replace("Ms. ", "")
		data=data.replace("Miss. ", "")    
		all_rows = all_rows + row_data.format(name=data, table=row[2])
		print(data, row[2])		
		nameList[counter]=data
		#print(data)
		counter=counter+1

write_data = header + all_rows + footer
outfile = open("lisitha.html","w")
outfile.write(write_data)
outfile.close()

# fileList = glob.glob("*.jpg")
# 248,249,252
##F8F9FC
# index=1
# for file in fileList:
	# print("Renaming " + file + " to " + nameList[index]+".jpg" + " (" + str(index) + "/" + str(len(fileList)) + ")")
	# os.rename(file,nameList[index]+".jpg")
	# index = index + 1