

export class PresentationService {

    isEmpty(obj: any) {
        return obj // null and undefined check
               && Object.keys(obj).length === 0
               && Object.getPrototypeOf(obj) === Object.prototype;
    }
    
    isParseable(rawData: string) {
        try {
          return JSON.parse(rawData);
        } catch(e) {
          return false;
        }
    }
    
    escapeHtml(unsafe: string) {
        return unsafe.replaceAll('&', '&amp;')
                     .replaceAll('<', '&lt;')
                     .replaceAll('>', '&gt;')
                     .replaceAll('"', '&quot;')
                     .replaceAll("'", '&#039;');
    }

}