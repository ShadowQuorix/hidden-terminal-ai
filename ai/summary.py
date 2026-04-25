class AISummery:

   @staticmethod
   def summarize(result):
      # simple safe summary ( no exploitation guidance)
      if "80/tcp" in result:
         return "Web service detected. Investigate inputs, endpoints, and authentication."
      
      if "445/tcp" in result:
         return "SMB detected. check shared resources and permissions."
      
      return "General enumeration completed. Review open services."