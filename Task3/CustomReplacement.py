   
import sabre

class CustomReplacement(sabre.Replacement):

    def check_replace(self, quality):
        buffer = self.session.get_buffer_contents()
        for i in range(2, len(buffer)):
            if buffer[i] <= quality:
                # return -ve index from end of buffer
                return (i - len(buffer), quality)
        # if we arrive here, no switching occurs
        return (None, 0)
    '''
    def check_replace(self, quality):
        buffer = self.session.get_buffer_contents()
        manifest = self.session.manifest
        bitrates = manifest.bitrates
        throughput = self.session.get_throughput()
        new_quality = 0
        while (new_quality + 1 < len(bitrates) and bitrates[new_quality + 1] <= throughput):
            new_quality += 1
        for i in range(2, len(buffer)):
            if buffer[i] < new_quality:
                # return -ve index from end of buffer
                return (i - len(buffer), new_quality)
        # if we arrive here, no switching occurs
        return (None, 0)
    '''
    