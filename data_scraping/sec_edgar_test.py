import sys
from crawler import SecCrawler
from multiprocessing import Pool as ThreadPool
import time 

def getSingleCompanyFiling(inputData):
	date = '20170313' # date from which filings should be downloaded 
	count = '100' # no of filings

	seccrawler = SecCrawler() 
	companyCode, cik = inputData
	t1 = time.time() 
	seccrawler.getFiling(str(companyCode), str(cik), str(date), str(count), "10-K")
	# seccrawler.getFiling(str(companyCode), str(cik), str(date), str(count), "10-Q")
	# seccrawler.getFiling(str(companyCode), str(cik), str(date), str(count), "8-K") 
	t2 = time.time()
	logString = "Total Time taken for " + companyCode + ": " + str(t2-t1)
	print logString
	return logString

def calculateParallel(inputs, threads=1):
    pool = ThreadPool(threads)
    results = pool.map(getSingleCompanyFiling, inputs)
    pool.close()
    pool.join()
    return results

def get_filings(num_threads): 
	# create object 
	# date = '20160922'

	start = time.time()
	sp_500 = open('sp_500.txt')
	lines = sp_500.readlines()
	sp_500.close()
	# companies = [line.split('\t')[1:3] for line in lines[0:4]]
	companies = [line.split('\t')[1:3] for line in lines]
	print 'GETTING THESE COMPANIES:' , companies

	companiesToDownload = 10
	curDownloaded = 0
	blocking = True
	scrapeCount = 0
	queries = [[companyCode, cik] for companyCode, cik in companies]

	results = calculateParallel(queries, num_threads)
	end = time.time()
	print '\n\n\n FINAL TIME:'
	print end - start
	# print queries
	# for companyCode, cik in companies:
	# 	# if companyCode != 'A' and blocking:
	# 	# 	scrapeCount += 1
	# 	# 	continue
	# 	# print 'madeit'
	# 	# blocking = False
	# 	# if scrapeCount < curDownloaded:
	# 		# scrapeCount += 1
	# 		# continue

	# 	t1 = time.time() 
	# 	seccrawler.getFiling(str(companyCode), str(cik), str(date), str(count), "10-K")
	# 	# seccrawler.getFiling(str(companyCode), str(cik), str(date), str(count), "10-Q")
	# 	# seccrawler.getFiling(str(companyCode), str(cik), str(date), str(count), "8-K") 
	# 	t2 = time.time() 
	# 	print "Total Time taken for ", companyCode, ": ", str(t2-t1)
	# 	# scrapeCount += 1
	# 	# if scrapeCount >= companiesToDownload:
	# 		# break

def nonthreaded_get_filings():
	# create object 
	seccrawler = SecCrawler() 
	date = '20170313' # date from which filings should be downloaded 
	# date = '20160922'

	count = '1' # no of filings

	sp_500 = open('sp_500.txt')
	lines = sp_500.readlines()
	sp_500.close()
	companies = [line.split('\t')[1:3] for line in lines]


	companiesToDownload = 10
	curDownloaded = 0
	blocking = True
	scrapeCount = 0
	
	start = time.time()
	for companyCode, cik in companies:
		# if companyCode != 'A' and blocking:
		# 	scrapeCount += 1
		# 	continue
		# print 'madeit'
		# blocking = False
		# if scrapeCount < curDownloaded:
			# scrapeCount += 1
			# continue

		t1 = time.time() 
		seccrawler.getFiling(str(companyCode), str(cik), str(date), str(count), "10-K")
		# seccrawler.getFiling(str(companyCode), str(cik), str(date), str(count), "10-Q")
		# seccrawler.getFiling(str(companyCode), str(cik), str(date), str(count), "8-K") 
		t2 = time.time() 
		print "Total Time taken for ", companyCode, ": ", str(t2-t1)
		# scrapeCount += 1
		# if scrapeCount >= companiesToDownload:
			# break
	end = time.time()
	print '\n\n\n FINAL TIME:'
	print end - start
	
if __name__ == '__main__':
	get_filings(int(sys.argv[1]))
	# nonthreaded_get_filings()