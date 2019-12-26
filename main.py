from args import get_args
from crawler import Crawler

if __name__ == '__main__':
    args = get_args() 
    crawler = Crawler()
    contents = crawler.crawl(args.start_date, args.end_date)
    # TODO: write content to file according to spec 
    f = open(args.output+'.csv','w')
    f.write('Post date,Title,Content\n')
    for date,title,content in contents:
        f.write('"'+date.replace('"','""')+'",') 
        f.write('"'+title.replace('"','""')+'",') 
        f.write('"'+''.join(content).replace('\r','').replace('\xa0','\n').replace('"','""')+'"\n')
    f.close()
